from conan.packager import ConanMultiPackager
import copy
import platform


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="Boost:shared", pure_c=False)
    builder.add(options={"Boost:header_only": True}, settings={'compiler': builder.builds[-1].settings['compiler']})
    if platform.system() == "Linux":
        filtered_builds = []
        for settings, options, env_vars, build_requires in builder.builds:
            filtered_builds.append([settings, options, env_vars, build_requires])
            new_options = copy.copy(options)
            new_options["Boost:fPIC"] = True
            filtered_builds.append([settings, new_options, env_vars, build_requires])
        builder.builds = filtered_builds
    builder.run()

