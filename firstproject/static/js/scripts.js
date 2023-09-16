/*!
* Start Bootstrap - Blog Home v5.0.8 (https://startbootstrap.com/template/blog-home)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-home/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

    // Add click event listener to toggle button
   
    //<!-- Map -->
   
    
    var map = L.map('map').setView([32.874199, -6.928924], 15);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors'
    }).addTo(map);
  
    L.marker([32.874199, -6.928924]).addTo(map).bindPopup("Group OCP - Khouribga");
  

//<!-- text -->

  // Add click event listener to toggle button
  document.getElementById("toggleBtn").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent default link behavior

    var moreText = document.getElementById("moreText");
    if (moreText.style.display === "none") {
      moreText.style.display = "inline";
      document.getElementById("toggleBtn").innerText = "Lire moins";
    } else {
      moreText.style.display = "none";
      document.getElementById("toggleBtn").innerText = "Lire la suite";
    }
  });



  document.getElementById("toggleBtn").addEventListener("click", function(e) {
    e.preventDefault();
    document.getElementById("moreText").style.display = "block";
    // Scroll to the expanded section
    document.getElementById("moreText").scrollIntoView({ behavior: "smooth" });
  });
