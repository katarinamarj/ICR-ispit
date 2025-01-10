import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-sixth-item',
  templateUrl: './sixth-item.component.html',
  styleUrl: './sixth-item.component.css'
})
export class SixthItemComponent {

  product = {
    id: 6,
    name: 'Thumper',
    price: 30,
    type: 'Rabbit',
    color: 'Grey',
    size: 'Small',
    origin: 'Canada',
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
