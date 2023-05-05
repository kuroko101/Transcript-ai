const form = document.querySelector('#transcription-form');
const transcriptionResult = document.querySelector('#transcription-result');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  const response = await fetch('/api/transcribe', {
    method: 'POST',
    body: formData,
  });
  const data = await response.json();
  transcriptionResult.innerText = data.transcription;
});
