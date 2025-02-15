function openModal(weaponName, weaponDetails, imageUrl) {
    // Assuming you already have a modal element
    const modal = document.getElementById("myModal");

    // Set the weapon name
    const modalTitle = document.getElementById("modalTitle");
    modalTitle.textContent = weaponName;

    // Set the weapon details
    const modalDetails = document.getElementById("modalDetails");
    modalDetails.textContent = weaponDetails;

    // Set the weapon image
    const modalImage = document.getElementById("modalImage");
    modalImage.src = imageUrl;

    // Show the modal
    modal.style.display = "block";
}

function closeModal() {
    const modal = document.getElementById("myModal");
    modal.style.display = "none";
}
window.onload = function() {
    const text = document.getElementById('text');
    const letters = text.innerText.split('');
    
    // Replace text content with spans around each letter
    text.innerHTML = letters.map(letter => `<span>${letter}</span>`).join('');
  };
  

  function openModal(title, details, imageUrl) {
    document.getElementById("modalTitle").innerText = title;
    document.getElementById("modalDetails").innerText = details;
    document.getElementById("modalImage").src = imageUrl;
    document.getElementById("myModal").style.display = "block";
  }
  
  function closeModal() {
    document.getElementById("myModal").style.display = "none";
  }
   