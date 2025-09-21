const express = require("express");
const axios = require("axios");
const bodyParser = require("body-parser");
const path = require("path"); 

const URL=process.env.BACKEND_URL || "http://localhost:5000/submit";

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, "public")));
app.get("/", (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.post("/submit", async (req, res) => {
  const { name, surname , email , message} = req.body;
  try {
    const response = await axios.post(URL, { name, surname, email, message });
    res.send(response.data);
  } catch (error) {
    console.error("Error details:", error.message);
    res.status(500).send("Error connecting to backend");
  }
});

app.get('/health', (req, res) => {
    res.status(200).json({
        status: 'healthy',
        service: 'frontend-express',
        timestamp: new Date().toISOString(),
        uptime: process.uptime()
    });
});

app.listen(3000, () => {
  console.log("Frontend running on port 3000");
});