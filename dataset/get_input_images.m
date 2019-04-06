path = [pwd '/BSR/BSDS500/data/groundTruth/'];
dest = [pwd '/input/'];
states = {'train/', 'val/', 'test/'};
mkdir('input');

for i = 1:length(states)
    file_list = dir(fullfile(path, states{i}, '*.mat'));
    for j = 1:length(file_list)
        [~, image_name, ~] = fileparts(file_list(j).name);
        load([path states{i} file_list(j).name]);
        bound = groundTruth{1}.Boundaries;
        imwrite(bound, [dest image_name '.jpg']);
    end
end
