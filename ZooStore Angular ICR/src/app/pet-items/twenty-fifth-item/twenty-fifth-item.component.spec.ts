import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TwentyFifthItemComponent } from './twenty-fifth-item.component';

describe('TwentyFifthItemComponent', () => {
  let component: TwentyFifthItemComponent;
  let fixture: ComponentFixture<TwentyFifthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TwentyFifthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TwentyFifthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
