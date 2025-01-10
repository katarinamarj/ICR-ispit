import { Component, ElementRef, HostListener } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrls: ['./payment.component.css'] 
})
export class PaymentComponent {
  cvvPattern = '^[0-9]{3}$';

  constructor(private el: ElementRef, private router: Router, private snackBar: MatSnackBar) {}

  @HostListener('input', ['$event'])
  onInput(event: any) {
    if (event.target.name === 'cardNumber') {
      let input = event.target.value;
      input = input.replace(/\D/g, '');

      if (input.length > 16) {
        input = input.substring(0, 16);
      }

      if (input.length > 0) {
        input = input.match(new RegExp('.{1,4}', 'g')).join(' ');
      }

      event.target.value = input;
    }
  }

  limitCVVInput(event: any) {
    let input = event.target.value.replace(/\D/g, '');

    if (input.length > 3) {
      input = input.substring(0, 3);
    }

    event.target.value = input;
  }

  onSubmit(form: NgForm) {
    if (form.valid) {
      this.snackBar.open('Payment successful', 'Close', {
        duration: 400,
      });

      setTimeout(() => {
        this.router.navigate(['/home']);
      }, 500); 
    } else {
      this.snackBar.open('Please fill in all fields correctly', 'Close', {
        duration: 900,
      });
    }
  }
}
