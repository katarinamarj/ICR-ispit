import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-ninth-item',
  templateUrl: './ninth-item.component.html',
  styleUrl: './ninth-item.component.css'
})
export class NinthItemComponent {

  product = {
    id: 9,
    name: 'Socks',
    price: 60,
    type: 'Cat',
    color: 'White',
    age: '3',
    size: 'Small',
    origin: 'UK',
    review: '5 stars',
    image: 'https://thumbs.dreamstime.com/b/turkish-angora-cat-white-background-portrait-animal-themes-front-view-145390427.jpg'
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
