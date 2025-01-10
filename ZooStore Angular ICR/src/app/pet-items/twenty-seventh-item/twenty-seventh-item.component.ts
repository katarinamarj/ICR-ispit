import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-twenty-seventh-item',
  templateUrl: './twenty-seventh-item.component.html',
  styleUrl: './twenty-seventh-item.component.css'
})
export class TwentySeventhItemComponent {

  product = {
    id: 27,
    name: 'Flare',
    price: 80,
    type: 'Cat',
    color: 'Gray',
    age: '2',
    size: 'Medium',
    origin: 'India',
    review: '5 stars',
    image: 'https://i.pinimg.com/550x/c1/c4/4a/c1c44a54126f793241da90e3d4c147e3.jpg'
  };
  constructor(private cartService: CartService, private router: Router) {}

  addToCart(product: any) {
    this.cartService.addToCart(product);
    this.router.navigate(['/cart']);
  }

}
