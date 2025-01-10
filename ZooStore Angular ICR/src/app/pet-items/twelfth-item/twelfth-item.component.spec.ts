import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TwelfthItemComponent } from './twelfth-item.component';

describe('TwelfthItemComponent', () => {
  let component: TwelfthItemComponent;
  let fixture: ComponentFixture<TwelfthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TwelfthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TwelfthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
