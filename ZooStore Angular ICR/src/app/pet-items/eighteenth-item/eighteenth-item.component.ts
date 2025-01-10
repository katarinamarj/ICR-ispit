import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CartService } from '../../cart.service';

@Component({
  selector: 'app-eighteenth-item',
  templateUrl: './eighteenth-item.component.html',
  styleUrl: './eighteenth-item.component.css'
})
export class EighteenthItemComponent {

  product = {
    id: 18,
    name: 'Flopsy',
    price: 40,
    type: 'Rabbit',
    color: 'White',
    age: '1',
    size: 'Medium',
    origin: 'Australia',
    review: '4 stars',
    image: 'https://media.istockphoto.com/id/959866606/photo/rabbit-4-months-old-sitting-against-white-background.jpg?s=612x612&w=0&k=20&c=8yRFVDIgoXj3gCh7ckkF4gCh8JjWN967r244PQ4vFUU='
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
