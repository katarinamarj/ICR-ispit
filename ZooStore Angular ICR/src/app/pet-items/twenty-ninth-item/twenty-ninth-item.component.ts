import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-twenty-ninth-item',
  templateUrl: './twenty-ninth-item.component.html',
  styleUrl: './twenty-ninth-item.component.css'
})
export class TwentyNinthItemComponent {

  product = {
    id: 29,
    name: 'Viper',
    price: 130,
    type: 'Snake',
    color: 'Brown',
    age: '3',
    size: 'Large',
    origin: 'India',
    review: '4 stars',
    image: 'https://img.freepik.com/premium-psd/brown-snake-white-background-isolated-white-transparent-png-generative-ai_130745-271.jpg'
  };
  constructor(private cartService: CartService, private router: Router) {}

  addToCart(product: any) {
    this.cartService.addToCart(product);
    this.router.navigate(['/cart']);
  }

}
