// Optional JavaScript for extra validation or UX enhancements
document.getElementById('loanForm').addEventListener('submit', function(e) {
  // Example: Validate phone length or other checks if needed
  const phone = document.getElementById('phone').value;
  if (phone.length < 10) {
    e.preventDefault();
    alert('Phone number should be at least 10 digits.');
  }
});
