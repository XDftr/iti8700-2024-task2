import os


class Converted:
    def __init__(self, input_folder, output_folder):
        self.convert_folder(input_folder, output_folder)

    def convert_rdf_line_to_logictools_format(self, line):
        parts = line.strip().split("\t")
        if len(parts) < 3:
            return None

        subject = parts[0].strip()
        predicate = parts[1].strip()
        obj = parts[2].strip().rstrip(" .")

        if obj.startswith('"'):
            obj = obj.split('"')[1]

        return f'triple("{subject}","{predicate}","{obj}").'

    def convert_file(self, input_filename, output_filename):
        with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w',
                                                                         encoding='utf-8') as outfile:
            for line in infile:
                converted_line = self.convert_rdf_line_to_logictools_format(line)
                if converted_line:
                    outfile.write(converted_line + '\n')

    def convert_folder(self, input_folder, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for filename in os.listdir(input_folder):
            if filename.endswith(".txt"):
                input_filename = os.path.join(input_folder, filename)
                output_filename = os.path.join(output_folder,
                                               f"{os.path.splitext(filename)[0]}_formatted{os.path.splitext(filename)[1]}")
                self.convert_file(input_filename, output_filename)
                print(f"Converted '{input_filename}' to '{output_filename}'")


if __name__ == "__main__":
    Converted("original_data", "formatted_data")
