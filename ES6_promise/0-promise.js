// 0-promise.js
function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
      // Perform asynchronous API request or any other async operation
      // For simplicity, let's resolve with a sample response after a delay
      setTimeout(() => {
        const sampleResponse = { data: "Sample API response" };
        resolve(sampleResponse);
      }, 1000); // Simulating a delay of 1 second
    });
  }
  
  export default getResponseFromAPI;