// Import necessary modules
const express = require("express");
const mongoose = require("mongoose");

// Create an Express application
const app = express();

// Connect to MongoDB (Assuming you have MongoDB running locally on the default port)
mongoose
  .connect("mongodb://localhost:27017/sampledb", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("Connected to MongoDB"))
  .catch((err) => console.error("Error connecting to MongoDB:", err));

// Define a schema for the data model (e.g., a simple 'Item' model)
const itemSchema = new mongoose.Schema({
  name: String,
  description: String,
});

// Define a model based on the schema
const Item = mongoose.model("Item", itemSchema);

// Define a route to handle incoming requests
app.get("/random-item", async (req, res) => {
  try {
    // Fetch a random item from the database
    const randomItem = await Item.aggregate([{ $sample: { size: 1 } }]);

    // Respond with the random item
    res.json(randomItem);
  } catch (err) {
    console.error("Error fetching random item:", err);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

// Start the server and listen on port 3000
const PORT = process.env.PORT || 3000;
app.listen(PORT, () =>
  console.log(`Server is running on http://localhost:${PORT}`)
);
