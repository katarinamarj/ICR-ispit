import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  registerUser(email: any, password: any, userProfile: { firstName: any; lastName: any; email: any; phone: any; address: any; favoriteItems: any; }) {
    throw new Error('Method not implemented.');
  }
  private loggedIn = false;
  private users: any[] = [
    {
      userEmail: 'nikola11@gmail.com',
      userPassword: 'Nikola11', 
      userProfile: {
        firstName: 'Nikola',
        lastName: 'Nikolic',
        email: 'nikola11@gmail.com',
        phone: '123-456-7890',
        address: '123 Street, City, Country',
        favoriteItems: 'Hamsters'
      }
    },
    {
      userEmail: 'marko22@gmail.com',
      userPassword: 'Marko222', 
      userProfile: {
        firstName: 'Marko',
        lastName: 'Markovic',
        email: 'marko22@gmail.com',
        phone: '987-654-3210',
        address: '456 Avenue, Town, Country',
        favoriteItems: 'Cats'
      }
    },
    {
      userEmail: 'jovana33@gmail.com',
      userPassword: 'Jovana33', 
      userProfile: {
        firstName: 'Jovana',
        lastName: 'Jovanovic',
        email: 'jovana33@gmail.com',
        phone: '555-123-7890',
        address: '789 Road, Village, Country',
        favoriteItems: 'Dogs'
      }
    },
      {
        userEmail: 'ana11@gmail.com',
        userPassword: 'Anaogr11', 
        userProfile: {
          firstName: 'Ana',
          lastName: 'Ogrizovic',
          email: 'ana11@gmail.com',
          phone: '+381658887202',
          address: 'Patrijarha Joanikija 17b',
          favoriteItems: 'Dogs'
        }
    },
    {
      userEmail: 'katarina02@gmail.com',
      userPassword: 'Katarina02', 
      userProfile: {
        firstName: 'Katarina',
        lastName: 'Marjanovic',
        email: 'katarina02@gmail.com',
        phone: '+381658887204',
        address: 'Patrijarha Joanikija 17v',
        favoriteItems: 'Snakes'
      }
  }

  ];
  userEmail: string | undefined;
  userPassword: string | undefined;
  userProfile: any;

  constructor(private router: Router) { }

  login(email: string, password: string) {
    // Provera da li korisnik postoji u listi korisnika
    const user = this.users.find(u => u.userEmail === email && u.userPassword === password);
    if (user) {
      this.loggedIn = true;
      this.userEmail = email;
      this.userPassword = password; // Čuvanje lozinke za prikazivanje
      this.userProfile = user.userProfile;
      this.router.navigate(['/userpanel']);
    } else {
      // Prikazati grešku ili obraditi situaciju kada korisnik ne postoji
      console.log('Pogrešan email ili lozinka');
    }
  }


  logout() {
    this.loggedIn = false;
    this.userEmail = '';
    this.userPassword = '';
    this.userProfile = {};
    this.router.navigate(['/login']);
  }

  isLoggedIn() {
    return this.loggedIn;
  }

  getUserEmail() {
    return this.userEmail;
  }

  getUserPassword() {
    return this.userPassword;
  }

  setUserPassword(newPassword: string) {
    this.userPassword = newPassword;
  }

  getUserProfile() {
    return this.userProfile;
  }

  updateUserProfile(profile: any) {
    this.userProfile = { ...this.userProfile, ...profile };
  }
}
