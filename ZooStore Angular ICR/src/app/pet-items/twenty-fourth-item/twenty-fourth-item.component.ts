import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-twenty-fourth-item',
  templateUrl: './twenty-fourth-item.component.html',
  styleUrl: './twenty-fourth-item.component.css'
})
export class TwentyFourthItemComponent {

  product = {
    id: 24,
    name: 'Thistle',
    price: 35,
    type: 'Rabbit',
    color: 'Orange',
    age: '1',
    size: 'Small',
    origin: 'New Zealand',
    review: '4 stars',
    image: 'https://www.collinsdictionary.com/images/full/rabbit_274039655.jpg'
  };


  constructor(private cartService: CartService, private router: Router) {}

  addToCart(product: any) {
    this.cartService.addToCart(product);
    this.router.navigate(['/cart']);
  }

}
