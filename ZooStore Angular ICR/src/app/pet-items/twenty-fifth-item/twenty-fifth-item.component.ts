import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-twenty-fifth-item',
  templateUrl: './twenty-fifth-item.component.html',
  styleUrl: './twenty-fifth-item.component.css'
})
export class TwentyFifthItemComponent {

  product = {
    id: 25,
    name: 'Fire',
    price: 155,
    type: 'Parrot',
    color: 'Green',
    age: '2',
    size: 'Medium',
    origin: 'Costa Rica',
    review: '5 stars',
    image: 'https://st.depositphotos.com/1578496/4368/i/450/depositphotos_43686969-stock-photo-beautiful-green-parrot.jpg'
  };

  constructor(private cartService: CartService, private router: Router) {}

  addToCart(product: any) {
    this.cartService.addToCart(product);
    this.router.navigate(['/cart']);
  }
}
