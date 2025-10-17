const API = 'http://localhost:8000'


// upload
document.getElementById('uploadForm').addEventListener('submit', async (e) => {
e.preventDefault();
const file = document.getElementById('file').files[0];
const name = document.getElementById('name').value;
const email = document.getElementById('email').value;
if (!file) { alert('select a file'); return; }
const fd = new FormData();
fd.append('file', file);
fd.append('name', name);
fd.append('email', email);
const res = await fetch(API + '/upload', { method: 'POST', body: fd });
const j = await res.json();
alert('Uploaded: ' + JSON.stringify(j));
});


// match
document.getElementById('matchBtn').addEventListener('click', async () => {
const job = document.getElementById('job').value;
const topk = document.getElementById('topk').value;
if (!job) { alert('paste a job description'); return; }
const res = await fetch(API + '/match', {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({ job_description: job, top_k: topk })
});
const j = await res.json();
const cont = document.getElementById('results');
cont.innerHTML = '';
j.results.forEach(r => {
const d = document.createElement('div');
d.innerHTML = `<b>${r.name || '—'}</b> (score: ${r.score.toFixed(3)}) — <a href="${API}/download/${r.id}">download</a>`;
cont.appendChild(d);
})
});
