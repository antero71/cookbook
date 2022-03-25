fn main() {
    let v = vec![1,2,3,4];

    print_vector(v);



    let mut v = vec![100, 32, 57];
    for i in &mut v {
        *i += 50;
    }

    print_vector(v);

   
}

fn print_vector(v: Vec<i32>){
    for i in &v {
        println!("{}",i);
    }
}
