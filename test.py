import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor


