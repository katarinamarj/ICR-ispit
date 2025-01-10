import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CartService } from '../../cart.service';

@Component({
  selector: 'app-sixteenth-item',
  templateUrl: './sixteenth-item.component.html',
  styleUrl: './sixteenth-item.component.css'
})
export class SixteenthItemComponent {

  product = {
    id: 16,
    name: 'Rio',
    price: 160,
    type: 'Parrot',
    color: 'Red',
    age: '5',
    size: 'Large',
    origin: 'Brazil',
    review: '5 stars',
    image: 'https://img.freepik.com/premium-photo/beautiful-parrot-white-background_41532-184.jpg'
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
