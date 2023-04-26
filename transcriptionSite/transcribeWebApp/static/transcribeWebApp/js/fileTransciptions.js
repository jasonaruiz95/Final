window.onload=function(){
const fileInput = document.querySelector('#fileupload input[type=file]');
  fileInput.onchange = () => {
    if (fileInput.files.length > 0) {
      const fileName = document.querySelector('#fileupload .file-name');
      fileName.textContent = fileInput.files[0].name;
    }
  }
}