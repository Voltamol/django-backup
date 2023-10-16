var loadFile = function(event) {
    var output = document.getElementById('output');
    output.src = URL.createObjectURL(event.target.files[0]);
      output.onload = function() {
        URL.revokeObjectURL(output.src) // free memory
      }
    
  };

  var docPreview = function(event) {
    var element = document.getElementById('doc-preview');
    element.innerText="hover to preview"
    // Get the Bootstrap tooltip instance
    const tooltip = bootstrap.Tooltip.getInstance(element);

    // Change the tooltip's content
    tooltip._config.title = event.target.files[0].name
    tooltip._setContent();

    // Update the tooltip
    tooltip.update();
  };

