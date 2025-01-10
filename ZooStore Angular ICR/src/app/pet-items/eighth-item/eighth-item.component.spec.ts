import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EighthItemComponent } from './eighth-item.component';

describe('EighthItemComponent', () => {
  let component: EighthItemComponent;
  let fixture: ComponentFixture<EighthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EighthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EighthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
