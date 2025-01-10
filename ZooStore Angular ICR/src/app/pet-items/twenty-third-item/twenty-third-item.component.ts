import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-twenty-third-item',
  templateUrl: './twenty-third-item.component.html',
  styleUrl: './twenty-third-item.component.css'
})
export class TwentyThirdItemComponent {

  product = {
    id: 23,
    name: 'Chester',
    price: 12,
    type: 'Hamster',
    color: 'Brown',
    age: '3',
    size: 'Small',
    origin: 'UK',
    review: '5 stars',
    image: 'https://static3.depositphotos.com/1003283/157/i/450/depositphotos_1574217-stock-photo-hamster.jpg'
  };


  constructor(private cartService: CartService, private router: Router) {}

  addToCart(product: any) {
    this.cartService.addToCart(product);
    this.router.navigate(['/cart']);
  }

}
