use std::io;

fn main() {
        loop {
            println!("Give a positive integer, max 187");
            println!("If you want exit, press q");

            let mut number = String::new();

            io::stdin().read_line(&mut number)
                .expect("Failed to read line");

            if number.trim().eq("q") {
                break;
            }

            let number: u32 = number.trim().parse()
                .expect("Please type a number!");

            if number > 187 {
                println!("Give number between 0 - 187");
            }

            println!("The {} th Fibonacci number are {}",number,fib(number));
    }
}

fn fib(number: u32) -> u128 {
    if number == 2 || number == 3 {
        return 1;
    }
    if number == 1 {
        return 0;
    }

    let mut fib_number: Vec<u128> = vec![0];
    fib_number.push(1);
    let mut counter = 2;
    let result = loop {
        fib_number.push(fib_number[counter-1]+fib_number[counter-2]);
        counter+=1;
        if counter == number as usize {
            break fib_number.pop().unwrap_or(0);
        }
    };
    result 
}
