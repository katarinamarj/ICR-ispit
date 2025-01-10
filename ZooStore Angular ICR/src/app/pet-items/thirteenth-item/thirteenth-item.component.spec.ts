import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ThirteenthItemComponent } from './thirteenth-item.component';

describe('ThirteenthItemComponent', () => {
  let component: ThirteenthItemComponent;
  let fixture: ComponentFixture<ThirteenthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ThirteenthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ThirteenthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
