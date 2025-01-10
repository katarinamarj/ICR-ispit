import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-eleventh-item',
  templateUrl: './eleventh-item.component.html',
  styleUrl: './eleventh-item.component.css'
})
export class EleventhItemComponent {

  product = {
    id: 11,
    name: 'Splash',
    price: 25,
    type: 'Fish',
    color: 'Gold',
    age: '2',
    size: 'Small',
    origin: 'China',
    review: '4 stars',
    image: 'https://s7d2.scene7.com/is/image/PetSmart/5176556'
  };

  constructor(
    private cartService: CartService, 
    private router: Router 
    ) {}

  addToCart(product: any) {
    this.cartService.addToCart(product);  
    alert('Product added to cart!');
    this.router.navigate(['/cart']);  
  }
}
