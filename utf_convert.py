KAN_DEV_CODE_POINT_DIFF = 896

special_character = [2385,2386,7386,32,3302,2404,3203, 2405,2365]

def translate_text(input_text,code_point_diff):
    output = ''
    for char in input_text:
        char_ord = ord(char)
        if char_ord not in special_character:
            char_ord -= code_point_diff
        output += chr(char_ord)

    return output


if __name__ == '__main__':
    print(translate_text('ಆಚಮನೀಯ', KAN_DEV_CODE_POINT_DIFF))
    print(translate_text('ನಮಸ್ಕಾರ', KAN_DEV_CODE_POINT_DIFF))

    gananamtva = 'ಗ॒ಣಾನಾ᳚೦ ತ್ವಾ ಗ॒ಣಪ॑ತಿಗ್೦ ಹವಾಮಹೇ ಕ॒ವಿ೦  ಕ॑ವೀ॒ನಾಮು॑ಪ॒ಮಶ್ರ॑ವಸ್ತಮ೦ । ಜ್ಯೇ॒ಷ್ಠ॒ರಾಜ॒೦ ಬ್ರಹ್ಮ॑ಣಾ೦ ಬ್ರಹ್ಮಣಸ್ಪತ॒ ಆ ನಃ॑ ಶೃ॑ಣ್ವನ್ನೂ॒ತಿಭಿ॑ಸ್ಸೀದ॒ ಸಾದ॑ನ೦ ॥'

    print(translate_text(gananamtva, KAN_DEV_CODE_POINT_DIFF))