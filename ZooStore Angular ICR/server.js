// server.js

const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Handlujte sa konekcijama
io.on('connection', (socket) => {
  console.log('A user connected');
  
  // Kada korisnik bude isključen
  socket.on('disconnect', () => {
    console.log('User disconnected');
  });
});

// Pokrenite server na portu 5005
server.listen(5005, () => {
  console.log('Server listening on http://localhost:5005');
});
