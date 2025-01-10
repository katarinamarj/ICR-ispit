import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-twenty-eighth-item',
  templateUrl: './twenty-eighth-item.component.html',
  styleUrl: './twenty-eighth-item.component.css'
})
export class TwentyEighthItemComponent {

  product = {
    id: 28,
    name: 'Buddy',
    price: 100,
    type: 'Dog',
    color: 'Brown',
    age: '3',
    size: 'Large',
    origin: 'France',
    review: '5 stars',
    image: 'https://img.freepik.com/free-psd/cute-brown-white-dog-scene_23-2150179279.jpg?semt=ais_hybrid'
  };

  constructor(private cartService: CartService, private router: Router) {}

  addToCart(product: any) {
    this.cartService.addToCart(product);
    this.router.navigate(['/cart']);
  }

}
