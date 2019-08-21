fn main() {
    
    let result = loop_test();
    assert_eq!(result, 20);
    println!("result is {}",result);
}

fn loop_test() -> u32 {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };
    result

}
