import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-signup',
  templateUrl:'./signup.component.html',
  styleUrl: './signup.component.css'
})

export class SignupComponent {
  f: any;

  onSubmit(form: NgForm){
    console.log(form);
  }

  emailPattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  phonePattern = '^\\+381[0-9]{7,9}$';
  passwordPattern = '^(?=.*[A-Z])(?=.*\\d).{8,}$';

}
