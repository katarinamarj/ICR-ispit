import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-seventh-item',
  templateUrl: './seventh-item.component.html',
  styleUrl: './seventh-item.component.css'
})
export class SeventhItemComponent {
  product = {
    id: 7,
    name: 'Max',
    price: 120,
    type: 'Dog',
    color: 'Brown',
    age: '5',
    size: 'Medium',
    origin: 'USA',
    review: '5 stars',
    image: 'https://www.bil-jac.com/media/sy5jgj4k/dog-leo-min.png?&format=webp&width=400&mode=max&quality=80'
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
