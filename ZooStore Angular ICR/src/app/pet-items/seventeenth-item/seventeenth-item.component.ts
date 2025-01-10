import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-seventeenth-item',
  templateUrl: './seventeenth-item.component.html',
  styleUrl: './seventeenth-item.component.css'
})
export class SeventeenthItemComponent {

  product = {
    id: 17,
    name: 'Fin',
    price: 30,
    type: 'Fish',
    color: 'Silver',
    age: '3',
    size: 'Medium',
    origin: 'Japan',
    review: '4 stars',
    image: 'https://allergy-web-staging.s3.ap-southeast-2.amazonaws.com/wp-content/uploads/Fish_600px_NoBKG.png'
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
