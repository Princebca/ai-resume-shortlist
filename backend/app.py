from flask import Flask, jsonify, request, send_from_directory
from sentence_transformers import util
from db import SessionLocal, Candidate, json_to_embedding, embedder  # adjust imports as needed

app = Flask(__name__)

@app.route('/list_candidates', methods=['GET'])
def list_candidates():
    session = SessionLocal()
    rows = session.query(Candidate).all()
    out = [{'id': r.id, 'name': r.name, 'email': r.email, 'filename': r.filename} for r in rows]
    session.close()
    return jsonify(out)


@app.route('/match', methods=['POST'])
def match_job():
    data = request.json
    job_text = data.get('job_description', '')
    top_k = int(data.get('top_k', 10))

    session = SessionLocal()
    candidates = session.query(Candidate).all()

    results = []
    job_emb = embedder.encode(job_text)[0]

    for c in candidates:
        emb = json_to_embedding(c.embedding)
        # cosine similarity
        sim = float(util.cos_sim(emb, job_emb).item())
        results.append({'id': c.id, 'name': c.name, 'email': c.email, 'score': sim})

    results = sorted(results, key=lambda x: x['score'], reverse=True)[:top_k]

    session.close()
    return jsonify({'results': results})


@app.route('/download/<int:cand_id>', methods=['GET'])
def download_resume(cand_id):
    session = SessionLocal()
    c = session.query(Candidate).filter(Candidate.id == cand_id).first()
    session.close()

    if not c:
        return jsonify({'error': 'not found'}), 404

    return send_from_directory(app.config['UPLOAD_FOLDER'], c.filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
