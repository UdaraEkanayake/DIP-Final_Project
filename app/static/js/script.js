// Function to display a preview of the selected image
function previewImage(event) {
    var fileInput = event.target;
    var file = fileInput.files[0];
    var reader = new FileReader();
  
    reader.onload = function() {
      var imgElement = document.getElementById("preview");
      imgElement.src = reader.result;
      imgElement.style.display = "block";
    };
  
    reader.readAsDataURL(file);
  }
  
  // Event listener for the file input element
  var fileInput = document.getElementById("imageInput");
  fileInput.addEventListener("change", previewImage);
  