import { Component } from '@angular/core';
import { AuthService } from './auth.service';
import { RasaService } from './rasa.service';  
import { NgFor, NgIf } from '@angular/common';
import { FormsModule } from '@angular/forms';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']  
})

export class AppComponent {
  constructor(public authService: AuthService, private rasaService: RasaService) { }

  logout() {
    this.authService.logout();
  }

  isChatOpen = false;
  userInput = '';
  messages = [
    { sender: 'bot', text: 'Hi! How can I assist you today?' }
  ];

  toggleChat() {
    this.isChatOpen = !this.isChatOpen;
  }

  sendMessage() {
    if (this.userInput.trim()) {
      this.messages.push({ sender: 'user', text: this.userInput });

      // Pozivamo Rasa API za slanje poruke
      this.rasaService.sendMessage(this.userInput).subscribe(
        (response) => {
          // Odgovor bota u chat
          response.forEach((msg: any) => {
            this.messages.push({ sender: 'bot', text: msg.text });
          });
        },
        (error) => {
          // Ako dođe do greške
          this.messages.push({ sender: 'bot', text: 'Sorry, I am having trouble.' });
        }
      );

      this.userInput = '';  // Reset unosa
    }
  }
}
