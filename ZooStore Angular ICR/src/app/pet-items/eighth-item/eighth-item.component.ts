import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-eighth-item',
  templateUrl: './eighth-item.component.html',
  styleUrl: './eighth-item.component.css'
})
export class EighthItemComponent {

  product = {
    id: 8,
    name: 'Nibbles',
    price: 15,
    type: 'Hamster',
    color: 'Brown',
    age: '1',
    size: 'Small',
    origin: 'USA',
    review: '4 stars',
    image: 'https://st4.depositphotos.com/10614052/41661/i/450/depositphotos_416618198-stock-photo-funny-hamster-white-background.jpg'
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
